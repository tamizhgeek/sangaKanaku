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

KanakuControllers.controller('KanakuExpenseController', ['$scope', '$routeParams', '$http',  function($scope,  $routeParams, $http) {
	$scope.houseId = $routeParams.houseId;
	$http.get('/api/house/'+$scope.houseId+'/expenses').success(function(data) {
		$scope.expenses = data;
	});
	
	$scope.delete = function(index) {
		expense = $scope.expenses[index];
		$http.delete('/api/expense/' + expense.id).success(function(data){
			$scope.expenses.splice(index, 1);
		});
	};
}]);

KanakuControllers.controller('KanakuExpenseEditController', 
														 ['$scope','$routeParams','$http', '$filter',
															function($scope, $routeParams, $http, $filter) {
																$scope.newExpense = {};
																$http.get('/api/house/?format=json').success(function(data) {
																	$scope.houseId = $routeParams.houseId;
																	$scope.houses = data;
																});
																$scope.save = function(expense) {
																	console.log(expense.date);
																	expense.house = expense.house.id;
																	expense.date = new Date(expense.date).toISOString();
																	$http.post('/api/expense/', expense).success(function(data) {
																		$('#messages').addClass('alert alert-success').append('<p>Success!</p>');
																		$scope.newExpense = {};
																	});
																}
															}
														 ]);

KanakuControllers.controller('KanakuHouseController', ['$scope', '$http',function($scope, $http) {
	$http.get('/api/house/?format=json').success(function(data) {
		$scope.houses = data;
	});
}]);


var KanakuApp = angular.module('KanakuApp', ['ngRoute', 'KanakuControllers']);

KanakuApp.config(['$routeProvider', 
					 function($routeProvider){
						 $routeProvider.
							 when('/house/:houseId/expenses', {
								 templateUrl: '/static/html/partials/expenses.html',
								 controller: 'KanakuExpenseController'
							 }).
							 when('/house', {
								 templateUrl: '/static/html/partials/houses.html',
								 controller: 'KanakuHouseController'
							 }).
							 when('/newExpense/:houseId', {
								 templateUrl: '/static/html/partials/newExpense.html',
								 controller: 'KanakuExpenseEditController'
							 }).
							 otherwise({
								redirectTo: '/house' 
							 });
						 
}]);
