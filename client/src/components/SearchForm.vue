<template>
  <div>
    <div>
        <input type="text" v-model="project" class="form-control" placeholder="search projects...">
        <ProviderSelect/>
        <PaginationSelect @changeSearchPagination="size = $event" />
        <div v-if="$apollo.queries.gitRepos.loading">Searching...</div>
        <div v-if="error">{{ error }}</div>
        <br/>
        <PaginatedList 
          v-if="gitRepoResults.length > 0" 
          :list="gitRepoResults" 
          :size="size" 
          :pageNumber="pageNumber" 
          @resetPageNumber="pageNumber = $event" />
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
        size: 10,
        pageNumber: 0,
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
        result ({ data }) {
            this.$emit('resetPageNumber', 0);
            return this.gitRepoResults = data.gitRepos.items;
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
    }
  }
</script>
