var app=angular.module("myApp",[]);
		app.controller('myCtrl',function($scope,$http){
		$scope.names = ['List Item 01','List Item 02','List Item 03','List Item 04','List Item 05','List Item 06','List Item 07'];
		$scope.PopUp=function(){	
			document.getElementById("myCard").style.display="inline"
		}
		$scope.closeDiv=function(){	
			document.getElementById("myCard").style.display="none"
		}
		});