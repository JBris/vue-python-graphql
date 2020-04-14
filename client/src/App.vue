<template>
  <div id="app" ref="app">
    <Header/>
    <SearchForm v-on:scroll_to_top="scrollToTop" />
  </div>
</template>

<script>
import Header from '@/components/layout/Header';
import SearchForm from '@/components/SearchForm';

export default {
  name: 'app',
  ele: '#app',
  components: {
    Header,
    SearchForm,
  },
  methods: {
    scrollToTop() {
      this.$refs.app.scrollIntoView()
    },
  },
}
</script>

<style lang="scss">
  @import "@/assets/styles/main.scss";
</style>