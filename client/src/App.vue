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
  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .footer-buttons {
    padding: 0.75rem;
    width: 100%;
  }
  @import "~bulma";
</style>