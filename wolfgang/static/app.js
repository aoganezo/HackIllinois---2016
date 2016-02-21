'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
        'ngRoute',
        'myApp.step1',
        'myApp.detail'
]).config([

    '$locationProvider',
    '$routeProvider',
    '$interpolateProvider',
    function ($locationProvider, $routeProvider, $interpolateProvider) {

      $interpolateProvider.startSymbol('{$');
      $interpolateProvider.endSymbol('$}');

      $routeProvider.otherwise({ redirectTo: '/' });

    }


]).factory('detailService', function () {

    var detail = "";

    function setDetail(id) {
        this.detail = id;
    }

    function getDetail() {
        return this.detail;
    }

    return {
        set: setDetail,
        get: getDetail
    }

});
