var app = angular.module('myapp',[]).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName - 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName - 'X-CSRFToken';
});

app.controller('myctrl',['$scope','$http',function($scope,$http){

    $scope.add = function(){
        var data = {
            'name':$scope.name,
            'address':$scope.address,
            'description':$scope.description
        };


        $http.post('http://127.0.0.1:8000/data/SubmitFir/',data).then(function(success){
                if(success.data.hasOwnProperty('error')){
                    swal({
                    title:"Warning!",
                    text:success.data.error,
                    type:"warning"
                    });
                }
                else{
                    swal({
                        title:"Success!",
                        text:"You have successfully registered and fir!",
                        type:"success"
                    });
                }
            },function(error){
                swal({
                    title: "Error",
                    text: "Some error was encountered while submitting your form.Please try after sometime.",
                    type: "error"
                });

        });
    };

}]);