const nextConfig = {
  webpack(config) {
    config.experiments = {
      asyncWebAssembly: true,
      layers: true,
    };

    return config;
  },
  OPENAI_API_KEY: process.env.OPENAI_API_KEY,
  SERP_API_KEY: process.env.SERP_API_KEY,
  PINECONE_API_KEY: process.env.PINECONE_API_KEY,
  PINECONE_INDEX: process.env.PINECONE_INDEX,
  PINECONE_ENVIRONMENT: process.env.PINECONE_ENVIRONMENT,
};

module.exports = nextConfig;
