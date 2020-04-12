<template>
  <div id="app">
    <Header/>
    <SearchForm/>
  </div>
</template>

<script>
import Header from './components/layout/Header';
import SearchForm from './components/SearchForm';
// import SearchResults from './components/SearchResults';
// import Pagination from './components/Pagination';

    //   <SearchResults
    //   v-if="videos.length > 0"
    //   v-bind:videos="videos"
    //   v-bind:reformattedSearchString="reformattedSearchString"
    // />
    // <Pagination
    //   v-if="videos.length > 0"
    //   v-bind:prevPageToken="api.prevPageToken"
    //   v-bind:nextPageToken="api.nextPageToken"
    //   v-on:prev-page="prevPage"
    //   v-on:next-page="nextPage"
    // />

export default {
  name: 'app',
  components: {
    Header,
    SearchForm,
    // SearchResults,
    // Pagination
  },
}
</script>