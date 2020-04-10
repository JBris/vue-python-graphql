import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import config from './config/config'

const httpLink = new HttpLink({
  // URL to graphql server, you should use an absolute URL here
  uri: `${config.HOST}/graphql`
})

// create the apollo client
const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache()
})

// install the vue plugin
Vue.use(VueApollo)

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
})

Vue.config.productionTip = false

// update Vue instance by adding `apolloProvider`
new Vue({
  el: '#app',
  router,
  apolloProvider,
  template: '<App/>',
  components: { App },
  render: h => h(App),
}).$mount('#app')
