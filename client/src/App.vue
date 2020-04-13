<template>
  <div id="app">
    <Header/>
    <SearchForm/>
  </div>
</template>

<script>
import Header from './components/layout/Header';
import SearchForm from './components/SearchForm';

export default {
  name: 'app',
  components: {
    Header,
    SearchForm,
  },
}
</script>