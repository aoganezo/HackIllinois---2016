'use strict';

angular.module('myApp.step1', ['ngRoute'])

.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
      templateUrl: '/static/views/step1/step1.html',
        controller: 'Step1Ctrl'
    });
}])

.controller('Step1Ctrl', ['$scope', '$http', '$location', 'detailService', function ($scope, $http, $location, detailService) {

  $http.get('https://127.0.0.1:8000/mainapp/getContacts')
            .success(function (data) {
                $scope.contacts = data;
            })
            .error(function () {
                alert("couldn't load data");
            });

  $scope.continue = function(id)
  {
    detailService.set(id);
    $location.path('details'); //navigate to second step
  }

}]);
