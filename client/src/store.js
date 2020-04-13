import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    provider: 'GITHUB',
    gitRepos: []
  },
  mutations: {
    setProvider(state, provider) {
      state.provider = provider;
    },
    setGitRepos(state, gitRepos) {
      state.gitRepos = gitRepos;
    }
  },
  actions: {

  }
})