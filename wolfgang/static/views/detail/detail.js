'use strict';

angular.module('myApp.detail', ['ngRoute'])

.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/details', {
      templateUrl: '/static/views/detail/detail.html',
        controller: 'DetailCtrl'
    });
}])

.controller('DetailCtrl', ['$scope', '$http', '$location', 'detailService', function ($scope, $http, $location, detailService) {

  $scope.detailid = detailService.get();

  $http.get('https://127.0.0.1:8000/mainapp/getUserInformation/?id=' + $scope.detailid )
            .success(function (data) {
              $scope.contact = data;
            })
            .error(function () {
                alert("couldn't load user info");
            });

    $.geolocation.get({win: function(position)
      {
        $scope.latitude = position.coords.latitude;
        $scope.longitude = position.coords.longitude;

        $http.get('https://127.0.0.1:8000/amadeus/nearestairport?longitude=' + $scope.longitude + "&latitude=" + $scope.latitude)
                  .success(function (data) {
                    $scope.nearestairport = data[data.length - 1];
                  })
                  .error(function () {
                      alert("couldn't find nearest airport");
                  });

        var geocoder = new google.maps.Geocoder();
        var address = $scope.contact[0]['MailingAddress']['street'] + " " + $scope.contact[0]['MailingAddress']['city']
                  + " " + $scope.contact[0]['MailingAddress']['state'] + " " + $scope.contact[0]['MailingAddress']['postalCode']
                  + " " + $scope.contact[0]['MailingAddress']['country'];

        geocoder.geocode( { 'address': address}, function(results, status) {

          if (status == google.maps.GeocoderStatus.OK) {
            var latitude = results[0].geometry.location.lat();
            var longitude = results[0].geometry.location.lng();


            $http.get('https://127.0.0.1:8000/amadeus/nearestairport?longitude=' + longitude + "&latitude=" + latitude)
                      .success(function (data) {
                        $scope.nearestdestairport = data[data.length - 1];


                        $http.get('https://127.0.0.1:8000/amadeus/search?origin=' + $scope.nearestairport['airport'] + "&destination=" + $scope.nearestdestairport['airport'])
                                  .success(function (data) {
                                    $scope.airportsdata = data;
                                  })
                                  .error(function () {
                                      alert("couldn't find airport search data");
                                  });



                      })
                      .error(function () {
                          alert("couldn't find nearest airport");
                      });



          }
        });




        $scope.$apply();
      },
      fail: function(error)
    {
      alert('cannot get location: ' + error);
    }});


}]);
