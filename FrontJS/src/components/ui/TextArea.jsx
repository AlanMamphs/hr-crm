import React, { Component } from "react";
import TextField from "@material-ui/core/TextField";
import { withStyles } from '@material-ui/core/styles';
import PropTypes from 'prop-types';

const styles = theme => ({
  textArea: {
    width: '100%'
  },
});

class TextArea extends Component {
  state = {
    multiline: "Controlled"
  };

  handleChange = name => event => {
    this.setState({
      [name]: event.target.value
    });
  };

  render() {
    const { classes } = this.props;
    return (
      <div>
        <TextField
          label={this.props.label}
          id="textArea-flexible"
          placeholder="введите текст"
          multiline
          rows="5"
          onChange={this.handleChange("multiline")}
          margin="normal"
          defaultValue={this.props.defaultValue}
          className={classes.textArea}
        />
      </div>
    );
  }
}

TextArea.propTypes = {
  classes: PropTypes.object.isRequired
};

export default withStyles(styles)(TextArea);