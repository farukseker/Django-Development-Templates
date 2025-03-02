# Base image olarak Bun'un resmi imajını kullanıyoruz
FROM oven/bun:1 as builder

# Çalışma dizinini belirle
WORKDIR /app

# package.json ve bun.lockb dosyalarını kopyala
COPY package.json bun.lockb ./

# Bağımlılıkları yükle
RUN bun install --frozen-lockfile

# Uygulama dosyalarını kopyala
COPY . .

# Nuxt uygulamasını build et
RUN bun run build

# Prod ortamı için temiz bir imaj oluşturuyoruz
FROM oven/bun:1 as runner

# Çalışma dizinini belirle
WORKDIR /app

# Builder aşamasından sadece gerekli dosyaları kopyala
COPY --from=builder /app ./

# Nuxt uygulamasını başlat
CMD ["bun", "run", "start"]
