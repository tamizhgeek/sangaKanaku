var app = angular.module('KanakuApp', [
    'ui.router',
    'restangular'
])

app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {

            url: "/",
            templateUrl: "/static/html/partials/_expense_list.html",
            controller: "ExpenseList"
        })

       .state('new', {

            url: "/new",
            templateUrl: "/expense-form",
            controller: "ExpnseCtrl"
        })
})

app.controller("ExpenseCtrl", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
function ($scope, Restangular, CbgenRestangular, $q) {


}])// end controller
