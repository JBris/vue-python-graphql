import { ApolloClient } from 'apollo-client'
import { ApolloLink } from 'apollo-link'
import { HttpLink } from 'apollo-link-http'
import { onError } from "apollo-link-error";
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import config from './config/config'

const errorLink = onError(e => console.log(e));

const httpLink = new HttpLink({
  // URL to graphql server, you should use an absolute URL here
  uri: `${config.HOST}/graphql`,
})

// create the apollo client
const apolloClient = new ApolloClient({
  link: ApolloLink.from([errorLink, httpLink]),
  cache: new InMemoryCache({
    dataIdFromObject: o => o['id']
  }),
})

// install the vue plugin
Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

Vue.config.productionTip = false

// update Vue instance by adding `apolloProvider`
new Vue({
  el: '#app',
  router,
  store,
  apolloProvider,
  template: '<App/>',
  components: { App },
  render: h => h(App),
}).$mount('#app')
