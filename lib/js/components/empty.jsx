var React = require('react');

class Empty extends React.Component{
    render(){
        return (
            <div id="info-text">
                {
                    (this.props.queried) ?
                        'Couldn\'t find Waldo' :
                        'Search Twitter & Wikipedia'
                }
            </div>
        );
    }
}

export default Empty;
