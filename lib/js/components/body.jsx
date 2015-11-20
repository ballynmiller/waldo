var React = require('react');
var $ = require('jquery');

var Body = React.createClass({
    render: function(){
        var feeds = this.props.data.map(function(feed){
            var i = 0;
            function createMarkup() { return {__html: feed.message}; };
            return (
                <div className='feed-item'>
                    <div id="app">{feed.application}</div>
                    <div id="text-container" dangerouslySetInnerHTML={createMarkup()} />
                </div>
            );
        });
        return (
            <div id="container">
                <div id="content">
                    {feeds}
                </div>
            </div>
        );
    }
});

export default Body;
