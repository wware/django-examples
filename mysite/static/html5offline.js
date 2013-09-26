var updateServer = function(url) {
    if (!!localStorage[url]) {
        // send cached data to server, let server decide whether to update itself
    }
};

var fetch = function(url, callback) {
    var xhr = new XMLHttpRequest();
    var maxWaitTime = 5000;  // milliseconds

    var noResponseTimer = setTimeout(function() {
        xhr.abort();
        if (localStorage['online_status']) {
            // fireEvent("offline", {});
            localStorage['onlineStatus'] = '0';
        }
        if (!!localStorage[url]) {
            callback(localStorage[url]);
        }
    }, maxWaitTime);

    xhr.onreadystatechange = function(event) {
        if (xhr.readyState < 4) {
            return;
        }
        clearTimeout(noResponseTimer);
        if (localStorage['online_status'] !== '1') {
            updateServer(url);
            localStorage['onlineStatus'] = '1';
        }

        if (xhr.status === 200) {
            localStorage[url] = xhr.responseText;
            callback(xhr.responseText);
        }
        else if (!!localStorage[url]) {
            // Error: apply callback to cached data if available.
            callback(localStorage[url]);
        }
    };
    xhr.open("GET", url, true);
    xhr.send();
};

var Pair = function(op, callback, data) {
    var url = '/html5offline/api/v1/pair/?format=json';
    if (op === 'get') {
        if (navigator.onLine) {
            // TODO if we were offline before, we should sync with the server now
            $.get(url, function(data) {
                localStorage[url] = data.objects;
                if (callback) {
                    callback(data.objects);
                }
            });
        } else {
            if (callback && localStorage[url]) {
                callback(localStorage[url]);
            }
        }
    } else if (op === 'post') {
        // data = $.each(data, function(item) {
        //     return {key:item.key, value:item.value};
        // });
        // data = JSON.stringify(data);
        if (navigator.onLine) {
            // TODO if we were offline before, we should sync with the server now
            $.ajax({
                type: 'POST',
                url: url,
                data: JSON.stringify({items: data}),
                dataType: "application/json",
                // processData:  false,
                contentType: "application/json"
            });
        } else {
            localStorage[url] = data;
        }
    } else {
        // TODO: PUT, DELETE
        alert('Not implemented yet: ' + op);
    }
};

var OfflineCtrl = function($scope) {
    $scope.newKey = '';
    $scope.newValue = '';
    $scope.items = [];

    $scope.getPairs = function() {
        Pair('get', function(data) {
            $scope.items = data;
        });
    };

    $scope.addPair = function() {
        $scope.items.push({key:$scope.newKey, value:$scope.newValue});
        $scope.newKey = '';
        $scope.newValue = '';
        Pair('post', null, $scope.items);
    };
};
