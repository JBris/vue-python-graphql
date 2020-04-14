<template>
  <div>
    <div>
        <input 
          type="text" 
          v-model="project" 
          class="form-control" 
          placeholder="Search projects..."
          v-on:keyup="clearResults"
        >
        <ProviderSelect v-on:change_provider="clearResults"/>
        <PaginationSelect/>
        <div v-if="isSearching === true">Searching...</div>
        <div v-if="error">{{ error }}</div>
        <div class="results-message">
          <p>{{ resultsMessage }}</p>
        </div>
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
        debounce: 300, 
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
