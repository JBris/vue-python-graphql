<template>
  <div class="paginated-list" >
      <div class="row">
        <ListItem class="col-md-3" 
          v-for="repo in paginatedData"   
          v-bind:repo="repo" 
          v-bind:key="repo.id" 
          v-bind:index="repo.id"
        />
      </div>
    <br/>
    <p>Page {{ pageNumber + 1 }}</p>
    <button :disabled="pageNumber === 0" @click="prevPage">
      Previous
    </button>
    <button :disabled="pageNumber >= pageCount -1" @click="nextPage">
      Next
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
    props:{
      list:{
        type:Array,
        required:true
      },
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
  .page-link {
    box-shadow: none !important;
  }
</style>
