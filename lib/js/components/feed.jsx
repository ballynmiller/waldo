var React = require('react');

class Feed extends React.Component {
    render(){
        var feed = this.props.results.map((data) => {
            return (
                <div className='feed-item'>
                    <div id="app">{data.application}</div>
                    <div id="text-container">{data.message}</div>
                </div>
            );
        });

        return (
             <div id="container">
                 <div id="content">
                     {feed}
                 </div>
             </div>
         );
    }
}

export default Feed;
