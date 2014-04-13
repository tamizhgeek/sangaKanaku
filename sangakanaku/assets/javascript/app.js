// var resource = angular.resource('KanakuResource', ['ngResource']);

// resource.factory('Expense', [$resource, function($resource){
// 	$resource('/api/expense/:id', id:, '@id'
// }]

// resource.factory('House', [$resource, function($resource){
// 	$resource('/api/house/:id', id:, '@id'
// }]

// resource.factory('HouseExpense', [$resource, function($resource){
// 	$resource('/api/House/:id/expenses/', id:, '@id'
// }]

var KanakuControllers = angular.module('KanakuControllers', []);

KanakuControllers.controller('KanakuExpenseController', function($scope,  $routeParams, $http) {
	$scope.houseId = $routeParams.houseId;
	$http.get('/api/house/'+$scope.houseId+'/expenses').success(function(data) {
		$scope.expenses = data;
	});
});

KanakuControllers.controller('KanakuHouseController', function($scope, $http) {
	$http.get('/api/house/?format=json').success(function(data) {
		$scope.houses = data;
	});
});


var KanakuApp = angular.module('KanakuApp', ['ngRoute', 'KanakuControllers']);

KanakuApp.config(['$routeProvider', 
					 function($routeProvider){
						 $routeProvider.
							 when('/house/:houseId/expenses', {
								 templateUrl: 'partials/expenses',
								 controller: 'KanakuExpenseController'
							 }).
							 when('/house', {
								 templateUrl: 'partials/houses',
								 controller: 'KanakuHouseController'
							 }).
							 otherwise({
								redirectTo: '/house' 
							 });
						 
}]);
