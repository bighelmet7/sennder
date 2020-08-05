import React, { useEffect, useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItemText";
import Divider from "@material-ui/core/Divider";
import axios from "axios";

function App({ url }) {
  const [movies, setMovies] = useState([]);
  const [error, setHasError] = useState(false);
  const refetchTiming = 3000;

  const useStyles = makeStyles((theme) => ({
    root: {
      padding: 20,
      backgroundColor: theme.palette.background.paper,
    },
    movieContainer: {
      width: "100%",
      maxWidth: 360,
      margin: "0 auto",
      backgroundColor: theme.palette.background.default,
    },
  }));

  const renderMovies = (list) =>
    list.map(({ title, people }) => (
      <List component="nav" aria-label="movie list">
        <ListItem button>
          <ListItemText primary={title} />
        </ListItem>
        {people.map((person) => (
          <ListItem button>
            <ListItemText secondary={person} />
          </ListItem>
        ))}
        <Divider />
      </List>
    ));

  const classes = useStyles();

  useEffect(() => {
    setInterval(
      () =>
        axios
          .get(url)
          .then(({ data }) => {
            console.log("App -> data", data);
            setMovies(data);
          })
          .catch(() => {
            setHasError(true);
          }),
      refetchTiming
    );
  }, [url]);

  return (
    <div className={classes.root}>
      <div className={classes.movieContainer}>
        {(error && (
          <div>
            Something went wrong...
            <span role="img" aria-labelledby="sad emoji">
              😔
            </span>
          </div>
        )) ||
          renderMovies(movies)}
      </div>
    </div>
  );
}

export default App;
