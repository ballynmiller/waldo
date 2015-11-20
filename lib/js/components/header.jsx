var React = require('react');
var classNames = require('classnames');

class Header extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            text: sessionStorage.getItem("text") || '',
        }

        this._bind('handleTextChange', 'searchHandler');

    }

    _bind(...methods){
        methods.forEach(method => this[method] = this[method].bind(this));
    }

    handleTextChange(e) {
        this.setState({text: e.target.value});
    }

    searchHandler(){
        this.props.searchHandler(this.state.text);
    }

    render(){
        var loadingContainerClasses = classNames({
            'visible': this.props.loading
        });

        return(
            <header>
                <div id="header-body">
                    <div id="header-title">{'Where\'s Waldo'}</div>
                    <div className="pure-form" id="form-container">
                        <input type="text"
                            placeholder="Enter search text"
                            onChange={this.handleTextChange}
                            value={this.state.text}>
                        </input>
                        <button
                            className="pure-button pure-button-primary"
                            onClick={this.searchHandler}>Submit
                        </button>
                        <div id="loading-container" className={loadingContainerClasses}>
                            <div className="loader">
                                <span className="a"></span>
                                <span className="b spin">
                                    <span className="c"></span>
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        )
    }
}

export default Header;
