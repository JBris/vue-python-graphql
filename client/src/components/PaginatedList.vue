<template>
  <div>
    <ul>
      <li v-for="p in paginatedData" v-bind:key="p.suffix">
        {{p.first}} 
        {{p.last}}  
        {{p.suffix}}
      </li>
    </ul>
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
    data () {
      return {
        pageNumber: 0
      }
    },
    props:{
      list:{
        type:Array,
        required:true
      },
      size:{
        type:Number,
        required:false,
        default: 1
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
        return Math.ceil(l/s);
      },
      paginatedData() {
        const start = this.pageNumber * this.size;
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
