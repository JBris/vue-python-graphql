<template>
  <div>
    <div>
        Search
        <!-- 1 -->
        <input type="text" v-model="project" class="form-control" placeholder="search projects...">
        <ProviderSelect/>
        <PaginationSelect @changeSearchPagination="quantity = $event" />
        <div v-if="$apollo.queries.gitRepos.loading">Searching...</div>
        <div v-if="error">{{ error }}</div>
        <PaginatedList :list="[]" />
        <div class="row">
            <div class="col-md-3" v-for="repo in gitRepoResults" v-bind:key="`${repo.id}-${repo.author}`">
                <div class="panel panel-default">
                    <div class="panel-heading">
                    <!-- display the city name and country  -->
                        <p>{{ repo.repo }}</p>
                        <p>{{ repo.author }}</p>
                    </div>
                    <div class="panel-body">
                    <!-- display the latitude and longitude of the city  -->
                        <p>{{ repo.htmlUrl }}</p>
                        <p>{{ repo.description }}</p>
                    </div>
                </div>
            </div>
        </div>

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
        quantity: 25,
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
            this.gitRepoResults = data.gitRepos.items;
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
