
var app = angular.module('ezreg');
app.requires.push('ui.tinymce');
app.controller('PriceController', ['$scope','$http','growl','Price','PaymentProcessor', PriceController])
.controller('EventPageController', ['$scope','$http','growl','EventPage', EventPageController])

function PriceController($scope,$http,growl,Price,PaymentProcessor) {
	var defaults={};
	var event_processors_url = null;
	var errorMessageHandler = function(response){
		growl.error(response.data.error ,{ttl: 5000});
	};
	$scope.selected_processors={};
	$scope.init = function(params){
		$scope.event_id = params.event_id;
		$scope.group = params.group;
		event_processors_url = params.event_processors_url;
		$scope.prices = Price.query({event:$scope.event_id});
		$scope.processors = PaymentProcessor.query({group:$scope.group});
		$http.get(event_processors_url).then(function(response){
			console.log('proc',response.data);
			$scope.selected_processors = response.data.processors;
		});
	}
	$scope.addPrice = function(){
		$scope.prices.push(new Price({'event':$scope.event_id}));
	}
	$scope.savePrices = function(){
		
		angular.forEach($scope.prices, function(price, key) {
			var success = function(response){
				console.log('success',response);
			}
			var error = function(response,stuff){
				console.log('error',response,price);
				price.errors = response.data;
			}
			
			if (price.id)
				price.$save(success,error);
			else
				price.$create(success,error);
		});
	}
	$scope.deletePrice = function(price,index){
		if(!price.id){
			$scope.prices.splice(index,1);
			return;
		}
		if(!confirm('Are you sure you want to delete this price?'))
			return;
		price.$delete(function(){
			$scope.prices.splice(index,1);
		});
	}
	$scope.saveProcessors = function(){
		console.log(event_processors_url,{'processors':$scope.selected_processors});
		$http.post(event_processors_url,{'processors':$scope.selected_processors}).then(
				function(response){
					growl.success("Payment processors updated",{ttl: 5000});
				},
				errorMessageHandler
		);
	}

}

function EventPageController($scope,$http,growl,EventPage) {
	$scope.init = function(params){
		$scope.event_id = params.event_id;
		$scope.pages = EventPage.query({event:$scope.event_id});
	}	
	$scope.addPage = function(){
		$scope.pages.push(new EventPage({event:$scope.event_id,heading:'New page'}));
	}
	$scope.savePage = function(page){
		if (page.id)
			page.$save()
		else
			page.$create()
	}
	$scope.deletePage = function(page,index){
		if(!confirm('Are you sure you want to delete this page?'))
			return;
		if(!page.id){
			$scope.pages.splice(index,1);
			return;
		}
		page.$delete(function(){
			$scope.pages.splice(index,1);
		});
	}

}