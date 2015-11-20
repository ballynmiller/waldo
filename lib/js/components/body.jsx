var React = require('react');
var $ = require('jquery');

import Empty from './empty';
import Feed  from './feed';

class Body extends React.Component {
    render(){
        var content = (this.props.results.length === 0) ?
            <Empty queried={this.props.queried} /> :
            <Feed  results={this.props.results} />;

        return (
            <div>{content}</div>
        );
    }
}

export default Body;
