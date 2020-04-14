<template>
  <div>
    <CollapsibleCard :title="`${repo.author}/${repo.repo}`" id="`repo-item-${repo.id}`">
        <div class="panel-body">
          <p class="list-item-details">{{ repo.description }}</p>
          <a :href="repo.htmlUrl" class = "list-item-details" :target="`_blank`" rel="noopener noreferrer">Home</a>
          <a :href="repo.tagsUrl" class = "list-item-details" :target="`_blank`" rel="noopener noreferrer">Tags</a>
          <a :href="repo.cloneUrl" class = "list-item-details" :target="`_blank`" rel="noopener noreferrer">Clone</a>
        </div>  
    </CollapsibleCard>
  </div>
</template>

<script>
  import CollapsibleCard from "@/components/CollapsibleCard.vue";
  
  export default {
    name: 'ListItem',
    components: {
      CollapsibleCard
    },
    props:{
      repo:{
        type : Object,
        required:true
      },
    },
  };
</script>

<style scoped>
  .list-item-details {
    margin-left: 5em;
    margin-right: 6em;
    margin-bottom: 2em;
    margin-top: 0.5em;
  }
</style>
