import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    provider: 'GITHUB',
    gitRepos: [],
    searchPageNumber: 0,
    searchListSize: 10,
  },
  mutations: {
    setProvider(state, provider) {
      state.provider = provider;
    },
    setGitRepos(state, gitRepos) {
      state.gitRepos = gitRepos;
    },
    incrementSearchPageNumber(state) {
      state.searchPageNumber++;
    },
    decrementSearchPageNumber(state) {
      state.searchPageNumber--;
    },
    resetSearchPageNumber(state) {
      state.searchPageNumber = 0;
    },
    setSearchListSize(state, searchListSize) {
      state.searchListSize = searchListSize;
    },
  },
  actions: {

  }
})