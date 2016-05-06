angular.module('app.controllers', [])
  

.controller('uKClimateAppCtrl', function($scope, $state, ClimateService) {
	$scope.data = {
		regionSelect: null,
		typeSelect: null,
		yearSelect: null,
	}
	
	$scope.nextPage = function() {
		if (
			$scope.data.regionSelect != null &&
			$scope.data.typeSelect != null &&
			$scope.data.yearSelect != null
		) {
			data = $scope.data;
			$state.go('uKClimateApp2', {data: $scope.data, months: $scope.months});
		}
	}
	
	ClimateService.getOptions(function(options){
		$scope.regions = options.data.region;
		$scope.types = options.data.type;
		$scope.years = options.data.year;
		$scope.months = options.data.month;
    });
	
})
   
.controller('uKClimateApp2Ctrl', function($scope, ClimateService) {
	console.log($scope.$$prevSibling);
	
	ClimateService.getClimateData($scope.$$prevSibling.data, function(res) {
		chart_data = []
		
		for (var d in res.data) {
			chart_data.push(res.data[d].data);
		}
		console.log(chart_data)
			
		new Chartist.Line('.ct-chart', {
			labels: $scope.months,
			series: [ chart_data ]
		});
	});

})
 
.service('ClimateService', function($http){
	var site = 'https://on-device-research-test-josh1313.c9users.io/climate/';
    return {
        getOptions: function(callback){
            return $http.get(site+'options').then(callback);
        },
		
		getClimateData: function(data, callback) {
			var get_query = '?region=' + data.regionSelect;
			get_query += '&type=' + data.typeSelect;
			get_query += '&year=' + data.yearSelect;
			console.log(get_query);
			
			var url = site+get_query;
			console.log(url);
			
			return $http.get(url).then(callback);
		}
	}
});
