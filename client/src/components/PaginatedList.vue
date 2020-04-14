<template>
  <div class="paginated-list" >
      <div class="row">   
        <ListItem class="columns is-vcentered has-text-centered"
          v-for="repo in paginatedData"   
          v-bind:repo="repo" 
          v-bind:key="repo.id" 
          v-bind:index="repo.id"
        />
      </div>
    <p>Page {{ pageNumber + 1 }}</p>
    <button 
      :disabled="pageNumber === 0" 
      class="button is-primary is-normal is-rounded pagination-button"
      @click="prevPage"
    >
      <p>Previous</p>
    </button>
    <button 
      :disabled="pageNumber >= pageCount -1" 
      class="button is-primary is-normal is-rounded pagination-button"
      @click="nextPage"
    >
      <p>Next</p>
    </button>
  </div>
</template>

<script>
  import ListItem from '@/components/ListItem.vue'

  export default {
    name: 'PaginatedList',
    components:{
      ListItem,
    },
    methods: {
      nextPage() {
        this.$emit('scroll_to_top');
        this.$store.commit('incrementSearchPageNumber');
      },
      prevPage(){
        this.$emit('scroll_to_top');
        this.$store.commit('decrementSearchPageNumber');
      },
    },
    computed: {
      list() {
        return this.$store.state.gitRepos
      },
      pageCount() {
        let l = this.list.length,
            s = this.size;
        return Math.floor(l/s);
      },
      paginatedData() {
        let start = this.pageNumber * this.size;
        const len = this.list.length -1;
        if (start < 0) { start = 0; }
        if (start > len ) { start = len - this.size; }
        const end = start + this.size;     
        return this.list.slice(start, end);
      },
      size() {
        return this.$store.state.searchListSize
      },
      pageNumber() {
        return this.$store.state.searchPageNumber
      },
    }
  };
</script>

<style scoped>
  .pagination-button {
      width: 10%;
      display: inline-block;
  }
  .page-link {
    box-shadow: none !important;
  }
</style>
