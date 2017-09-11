// src/routes.js
const React = require('react');
const { Route, IndexRoute } = require('react-router');
const Layout = require('./components/Layout');
const IndexPage = require('./components/IndexPage');
const NotFoundPage = require('./components/NotFoundPage');

const routes = (
  <Route path="/" component={Layout}>
    <IndexRoute component={IndexPage}/>
    <Route path="*" component={NotFoundPage}/>
  </Route>
);

export default routes;
