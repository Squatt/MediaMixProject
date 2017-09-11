// src/server.js

const path            = require('path');
const Server          = require('http').Server;
const Express         = require('express');
const React           = require('react');
const renderToString  = require('react-dom/server').renderToString;
const match           = require('react-router').match;
const RouterContext   = require('react-router').RouterContext;
const routes          = require('./routes.jsx');
const NotFoundPage    = require('./components/NotFoundPage');


// initialize the server and configure support for ejs templates
const app = new Express();
const server = new Server(app);
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// define the folder that will be used for static assets
app.use(Express.static(path.join(__dirname, 'static')));

// universal routing and rendering
app.get('*', (req, res) => {
  match(
    { routes, location: req.url },
    (err, redirectLocation, renderProps) => {

      // in case of error display the error message
      if (err) {
        return res.status(500).send(err.message);
      }

      // in case of redirect propagate the redirect to the browser
      if (redirectLocation) {
        return res.redirect(302, redirectLocation.pathname + redirectLocation.search);
      }

      // generate the React markup for the current route
      let markup;
      if (renderProps) {
        // if the current route matched we have renderProps
        // markup = renderToString(React.<RouterContext {...renderProps}/>);
        markup = ReactDOM.renderToString(React.createElement(RoutingContext, renderProps))
      } else {
        // otherwise we can render a 404 page
        markup = ReactDOM.renderToString(React.createElement(NotFoundPage))
        // markup = renderToString(<NotFoundPage/>);
        res.status(404);
      }

      // render the index template with the embedded React markup
      return res.render('index', { markup });
    }
  );
});

// start the server
const port = process.env.PORT || 3000;
const env = process.env.NODE_ENV || 'production';
server.listen(port, err => {
  if (err) {
    return console.error(err);
  }
  console.info(`Server running on http://localhost:${port} [${env}]`);
});
