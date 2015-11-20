var express = require("express");

app = express()

app.use(express.static('dist'));
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get("/", function(req, res){
    res.sendFile("dist/index.html", { root: __dirname} );
})

var server = app.listen(3000, function(){
    var host = server.address().address;
    var port = server.address().port;

    console.log("Serving at http://%s:%s", host, port);
});
