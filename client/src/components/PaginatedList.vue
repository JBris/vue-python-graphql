<template>
  <div class="paginated-list" @resetPageNumber="pageNumber = $event">
      <div class="row">
          <div class="col-md-3" v-for="(repo, key, index) in paginatedData" v-bind:key="index">
              <div class="panel panel-default">
                  <div class="panel-heading">
                      <p>{{ repo.repo }}</p>
                      <p>{{ repo.author }}</p>
                  </div>
                  <div class="panel-body">
                      <p>{{ repo.htmlUrl }}</p>
                      <p>{{ repo.description }}</p>
                  </div>
              </div>
          </div>
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
  export default {
    name: 'PaginatedList',
    props:{
      list:{
        type:Array,
        required:true
      },
      size:{
        type:Number,
        required:false,
        default: 10
      },
      pageNumber:{
        type:Number,
        required:false,
        default: 0
      },
    },
    methods: {
      nextPage() {
         this.pageNumber++;
      },
      prevPage(){
        this.pageNumber--;
      }
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
      }
    }
  };
</script>

<style scoped>
  .page-link {
    box-shadow: none !important;
  }
</style>
