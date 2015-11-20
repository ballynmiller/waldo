var React = require('react');

var Header = React.createClass({
    getInitialState: function(){
        return {text: sessionStorage.getItem("text") || ""};
    },
    handleClick(){
        this.props.handleClick(this.state.text);
    },
    handleTextChange(e) {
      this.setState({text: e.target.value});
    },
    render: function(){
        return(
            <header>
                <div
                    id="header-bg"
                >
                    <div id="logo">
                        <div id="logo-text">Where's Waldo
                            <div>
                                <input
                                    type="text"
                                    placeholder="Enter search"
                                    value={this.state.text}
                                    onChange={this.handleTextChange}
                                ></input>
                                <button
                                    onClick={this.handleClick}
                                >
                                    Submit
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        )
    }
});

export default Header;
