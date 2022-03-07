import { resolve } from 'path'
import { readdirSync } from 'fs'
import handlebars from 'vite-plugin-handlebars'

let partials = resolve(__dirname, 'partials')
let project_files = readdirSync(partials).filter((file) => file.startsWith("proj"))

export default {
    plugins: [
        handlebars({
            partialDirectory: partials,
            context: {
                projects: project_files
            }
        }),
    ],
}
