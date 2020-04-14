<template>
    <div>
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-half">
            <div class="field search-input is-5">
            <label class="label">Project</label>
            <div class="control">
              <input 
                type="text" 
                v-model="project" 
                class="input is-normal is-primary is-rounded" 
                placeholder="Search projects..."
                v-on:keyup="clearResults"
              >
            </div>
          </div> 

          <div class="level options-level">
            <div class="level-left">
              <ProviderSelect v-on:change_provider="clearResults"/>
            </div>
            <div class="level-right">
              <PaginationSelect/>
            </div>
          </div>
          
          <div class="container has-text-centered search-result-messages">
            <div v-if="isSearching === true">
              Searching...
              <progress class="progress is-small is-primary search-progress-bar" max="100">25%</progress>
            </div>
            <div v-if="error">{{ error }}</div>
            <div class="results-message">
              <p>{{ resultsMessage }}</p>
            </div>
          </div>

        </div>
      </div>
    </div>
        
    <div class="container">
      <PaginatedList 
        v-if="gitRepoResults.length > 0" 
        v-on:scroll_to_top="scrollToTop"
      />
    </div>

  </div>
</template>

<script>
  import { SEARCH_QUERY } from '@/graphql'
  import ProviderSelect from '@/components/ProviderSelect.vue'
  import PaginationSelect from '@/components/PaginationSelect.vue'
  import PaginatedList from '@/components/PaginatedList.vue'
  
  export default {
    name: 'SearchForm',
    data () {
      return {
        project: '',
        error: null,
        resultsMessage: "",
        isSearching: false,
      }
    },
    components:{
      ProviderSelect,
      PaginationSelect,
      PaginatedList,
    },
    apollo: {
      gitRepos: {
        query: SEARCH_QUERY,
        fetchPolicy: 'cache-and-network',
        variables () {
          return {
            provider: this.$store.state.provider,
            project: this.project,
            quantity: 50,
          }
        },
        watchLoading (isLoading) {
          if(isLoading) { this.clearResults(); }
        },
        result (res) {
            if (!res.data) { return; }
            this.isSearching = false;
            this.$store.commit('resetSearchPageNumber');
            this.gitRepoResults = res.data.gitRepos.items;
            const length = res.data.gitRepos.items.length;
            this.resultsMessage = `${length} results found.`;
        },
        options: () => ({ errorPolicy: 'all' }),
        skip () {
          return !this.project
        },
        error(error) {
            this.error = error.message;
        },
        debounce: 500, 
        errorPolicy: 'all',
        manual: true,
      }
    },
    computed: {
      gitRepoResults: {
        get () {
          return this.$store.state.gitRepos
        },
        set (value) {
          this.$store.commit('setGitRepos', value)
        }
      }
    },
    methods: {
      scrollToTop() {
        this.$emit('scroll_to_top');
      },
      clearResults() {
        this.resultsMessage = "";
        this.error = "";
        this.gitRepoResults = [];
        if(this.project) { this.isSearching = true; } 
      },
    },
  }
</script>

<style scoped>
  .search-input {
     margin: 0.5em;   
     width: 50vw;
  }
  .options-level {
    margin: 3em;
  }
  .search-result-messages {
    margin: 2em;
  }
  .search-progress-bar{
    width: 48vw;
  }
</style>