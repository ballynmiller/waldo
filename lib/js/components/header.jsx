var React = require('react');

var Header = React.createClass({
    render(){
        return (
            <header>
                <div>Where's Waldo?</div>
                <input type="text" placeholder="Enter search words"></input>
                <span>
                    <button>Sumbit</button>
                </span>
            </header>
        );
    }
});

export default Header;
