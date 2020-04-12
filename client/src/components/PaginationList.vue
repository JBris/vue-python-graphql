<template>
    <div class="pagination-list">
        <select v-model="quantity" @change="changeSearchPagination($event)">
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
        items: [10, 25, 50, 100],
        quantity: 25,
      }
    },
    methods: {
        changeSearchPagination(event) {
            this.$emit('changeSearchPagination', event.target.value)
        }
    }
  }
</script>
