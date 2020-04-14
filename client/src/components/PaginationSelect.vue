<template>
    <div class="pagination-list">
        <select v-model="size" @change="changeSearchPagination($event)">
          <option disabled value="">Results per page...</option>
          <option v-for="item in items" v-bind:key="item" v-bind:value="item">
            {{ item }}
          </option>
        </select>
    </div>
</template>

<script>
  export default {
    name: 'PaginationList',
    data () {
      return {
        items: [10, 25, 50],
        size: 10,
      }
    },
    methods: {
        changeSearchPagination(event) {
          const size = parseInt(event.target.value);
          this.$store.commit('setSearchListSize', size);
          this.$store.commit('resetSearchPageNumber')
        }
    }
  }
</script>
