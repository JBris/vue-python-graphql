<template>
  <div>
    <div>
        Search
        <!-- 1 -->
        <input type="text" v-model="project" class="form-control" placeholder="search...">
        <div v-if="$apollo.queries.gitRepos.loading">Searching...</div>
        <div v-if="error">{{ error }}</div>
        <div class="row">
            <div class="col-md-3" v-for="repo in gitRepos" v-bind:key="`${repo.id}-${repo.author}`">
                <div class="panel panel-default">
                    <div class="panel-heading">
                    <!-- display the city name and country  -->
                        {{ repo.repo }}: {{ repo.author }} 
                    </div>
                    <div class="panel-body">
                    <!-- display the latitude and longitude of the city  -->
                        <p>{{ repo.htmlUrl }},{{ repo.description }}.</p>
                    </div>
                </div>
            </div>
        </div>

    </div>
  </div>
  
</template>

<script>
  import { SEARCH_QUERY } from '@/graphql'

  export default {
    name: 'Search',
    data () {
      return {
        gitRepos: [],
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
            quantity: 50,
          }
        },
        update (data) {
            return data.gitRepos.items;
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
      }
    }
  }
</script>
