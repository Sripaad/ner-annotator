<template>
  <div>
    <section class="hero is-dark">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">NER Text Annotator</h1>
          <h2 class="subtitle">Annotate text for SpaCy NER Model training</h2>
        </div>
      </div>
    </section>

    <section class="hero">
      <div class="container">
        <div class="columns">
          <div class="column">
            <LoadTextFile class="pt-6" v-on:file-loaded="this.$emit('file-loaded');" />
          </div>
          <div class="column">
            <figure class="image" style="max-height: 15rem;">
              <img src="../assets/annotation.svg" />
            </figure>
          </div>
        </div>
      </div>
    </section>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
      <section class="hero is-dark">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Text Generation</h1>
          <h2 class="subtitle">Generate Sequence of text.</h2>
        </div>
      </div>
    </section>  
    <br>
    <br>
    <br>
    <section class="hero">
      <div class="container">
        <div class="columns">
          <div class="column">
            <button class="button is-danger is-outlined" @click="renderGenerationpage">generation page </button>
            <!-- <LoadTextFile class="pt-6" v-on:file-loaded="this.$emit('file-loaded');" /> -->
          </div>
          <div class="column">
            <figure class="image" style="max-height: 15rem;">
              <img src="../assets/generate_text.svg" />
            </figure>
          </div>
        </div>
      </div>
    </section>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
      <section class="hero is-dark">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">Text Classification</h1>
          <h2 class="subtitle">Classify emotions present in text.</h2>
        </div>
      </div>
    </section>  
    <br>
    <br>
    <br>
    <section class="hero">
      <div class="container">
        <div class="columns">
          <div class="column">
          <button class="button is-danger is-outlined" @click="renderClassificationpage">classification page</button>
            <!-- <LoadTextFile class="pt-6" v-on:file-loaded="this.$emit('file-loaded');" /> -->
          </div>
          <div class="column">
            <figure class="image" style="max-height: 15rem;">
              <img src="../assets/classification.svg" />
            </figure>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import LoadTextFile from "./LoadTextFile";
// import TextClassificationPage from "./TextClassificationPage";
// import SequenceGenerationPage from "./SequenceGenerationPage";

export default {
  name: "StartPage",
  emits: ["file-loaded", "classification-page", "generation-page"],
  components: {
    LoadTextFile,
    // TextClassificationPage,
    // SequenceGenerationPage,
  },
  methods: {
    onFileLoaded() {
      this.$emit("file-loaded");
    },

    renderClassificationpage() {
      this.$emit("classification-page");
    },

    renderGenerationpage() {
      this.$emit("generation-page")
    }
  },
};
</script>
