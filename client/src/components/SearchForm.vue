<template>
  <div>
    <div>
        Search
        <!-- 1 -->
        <input type="text" v-model="project" class="form-control" placeholder="search...">
        <div v-if="error">{{ error }}</div>
    </div>
  </div>
  
</template>

<script>

  // 2
  import { SEARCH_QUERY } from '@/graphql'

  export default {
    name: 'Search',
    data () {
      return {
        provider: 'GITHUB',
        project: '',
        error: null,
      }
    },
    apollo: {
      gitRepos: {
        query: SEARCH_QUERY,
        variables () {
          return {
            provider: this.provider,
            project: this.project,
            quantity: 100,
          }
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
      }
    }
  }
</script>
