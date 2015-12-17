var app = angular.module('myapp', []).config(function($interpolateProvider,$httpProvider){
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

app.controller('myctrl',['$scope','$http',function($scope,$http){
    $scope.posts = []
    $scope.load = function(){
        $scope.posts = [];
        var data = {
            'datestring':$scope.datestring
        };


        $http.post('http://127.0.0.1:8000/data/GetFir/',data).then(function(success){
                if(success.data.hasOwnProperty('error')){
                    swal({
                    title:"Warning!",
                    text:success.data.error,
                    type:"warning"
                    });
                }
                else{
                    $scope.datestring = '';
                    $scope.posts = success.data
                    if(success.data.length == 0){
                        swal({
                            title:'Oops!',
                            type:'warning',
                            text:'There were no FIRs in this date range'

                        });
                    }
                }
            },function(error){
                swal({
                    title: "Error",
                    text: "Some error was encountered while fetching the FIR's.Please try after sometime.",
                    type: "error"
                });
        });
    };

}]);