<template>
  <div class="column is-4">
    <CollapsibleCard :title="`${repo.author}/${repo.repo}`" id="`repo-item-${repo.id}`">
        <div class="panel-body">
            <p>{{ repo.htmlUrl }}</p>
            <p>{{ repo.description }}</p>
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
