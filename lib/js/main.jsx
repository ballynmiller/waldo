import Header from './components/header';

var $ = require('jquery')
var React = require('react');
var reactDom = require('react-dom');


var Waldo = React.createClass({
    render: function(){
        return (
            <div>
                <Header />
            </div>
        );
    }
});

reactDom.render(
        <Waldo />,
        $('#app').get(0)
);
