angular.module('app.controllers', [])
  
.controller('uKClimateAppCtrl', function($scope, ClimateService) {
	$scope.data = {
		regionSelect: null,
		typeSelect: null,
		yearSelect: null,
	}
	options = ClimateService.getOptions($scope);
	
})
   
.controller('uKClimateApp2Ctrl', function($scope, ClimateService) {
	var data = {
		labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
		series: [  [5, 2, 4, 2, 0] ]
	};
	new Chartist.Line('.ct-chart', data);

})
 
.service('ClimateService', function($http){
	var site = 'https://on-device-research-test-josh1313.c9users.io/climate/';
    return {
        getOptions: function($scope){
            return $http.get(site+'options').then(function(options) {
 				$scope.regions = options.data.region;
				$scope.types = options.data.type;
				$scope.years = options.data.year;
            });
        },
		
		getClimateData: function($scope) {
			return $http.get(site).then(function(data) {
				
			});
		}
	}
});
